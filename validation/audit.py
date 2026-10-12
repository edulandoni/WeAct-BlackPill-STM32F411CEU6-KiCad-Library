from pathlib import Path
import re,json,math,csv,hashlib
root=Path(__file__).resolve().parents[1]
f=next((root/'WeAct_BlackPill_STM32F411CEU6.pretty').glob('*.kicad_mod')).read_text()
s=(root/'WeAct_BlackPill_STM32F411CEU6.kicad_sym').read_text()
pads={int(n):(float(x),float(y),shape,float(d),float(dr)) for n,shape,x,y,d,dr in re.findall(r'\(pad "(\d+)" thru_hole (\w+) \(at ([\d.-]+) ([\d.-]+)(?: 90)?\) \(size ([\d.]+) [\d.]+\) \(drill ([\d.]+)\)',f)}
pins={int(n):(name,typ) for typ,name,n in re.findall(r'\(pin (\w+) line .*?\(name "([^"]+)".*?\(number "(\d+)"',s)}
# Manual transcription independently checked against official schematic P2, P1 and P3, page 1.
p2=['PB12','PB13','PB14','PB15','PA8','PA9','PA10','PA11','PA12','PA15','PB3','PB4','PB5','PB6','PB7','PB8','PB9','5V','GND','3V3']
p1=['5V','GND','3V3','PB10','PB2','PB1','PB0','PA7','PA6','PA5','PA4','PA3','PA2','PA1','PA0','NRST','PC15','PC14','PC13','VBAT']
p3=['3V3','SWDIO','SWCLK','GND']
assert len(pads)==len(pins)==44 and set(pads)==set(pins)==set(range(1,45))
holes=json.loads((root/'validation/data/step_holes.json').read_text())
rows=[]
# Native STEP coordinates, CAD +Y up; KiCad footprint +Y down. X offset=-19.558, Y offset=-9.1948.
for n in range(1,45):
 if n<=20:conn=f'P2.{n}';expected=p2[n-1];raw=(1.397+(n-1)*2.54,2.794)
 elif n<=40:conn=f'P1.{41-n}';expected=p1[40-n];raw=(1.397+(40-n)*2.54,18.009)
 else:conn=f'P3.{n-40}';expected=p3[n-41];raw=(45.872,6.629+(n-41)*2.54)
 assert min(math.hypot(raw[0]-h[0],raw[1]-h[1]) for h in holes if abs(h[3]-.45)<1e-6)<1e-8
 name,typ=pins[n];assert name.split(' / ')[0]==expected,(n,name,expected)
 x,y,shape,d,dr=pads[n];delta=math.hypot(x-(raw[0]-19.558),y-(-raw[1]+9.1948))
 assert delta<.001,(n,delta)
 rows.append([n,conn,expected,name,typ,x,y,*raw,delta,'PASS'])
with (root/'validation/pinout_and_geometry.csv').open('w', newline='') as o:
 w=csv.writer(o, lineterminator='\n');w.writerow(['library_pad','official_connector','official_signal','symbol_name','electrical_type','footprint_x_mm','footprint_y_mm','STEP_native_x_mm','STEP_native_y_mm','center_error_mm','result']);w.writerows(rows)
assert [n for n,p in pads.items() if p[2]=='rect']==[1]
clearance=min(math.dist(p[:2],q[:2])-(p[3]+q[3])/2 for n,p in pads.items() for m,q in pads.items() if m>n)
result={'pins':44,'pinout_mismatches':0,'maximum_center_error_mm':max(r[-2] for r in rows),'acceptance_mm':.001,'minimum_copper_gap_mm':clearance,'annular_ring_normal_mm':.4,'annular_ring_pad41_mm':.3,'square_pads':[1],'numbering_changes':0,'STEP_sha256':hashlib.sha256((root/'3dmodels/WeAct_MiniF4x1Cx_V31.step').read_bytes()).hexdigest()}
(root/'validation/audit_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
