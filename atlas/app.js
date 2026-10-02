'use strict';
(() => {
  const catalog = window.ASTRA_CATALOG;
  const demos = window.ASTRA_MODELS;
  const $ = id => document.getElementById(id);
  const projects = catalog.projects;
  const byId = new Map(projects.map(p => [p.id,p]));
  const sources = new Map(catalog.sources.map(s => [s.id,s]));
  let selected = byId.get(location.hash.slice(1)) || projects[0];
  let saved = new Set();
  try { saved = new Set(JSON.parse(localStorage.getItem('astra-saved-v1') || '[]').filter(x => byId.has(x))); } catch (_) { /* local persistence optional */ }
  let compared = [];
  function element(tag, text, className) {
    const e = document.createElement(tag);
    if (text !== undefined) e.textContent = text;
    if (className) e.className = className;
    return e;
  }
  function link(label, url) {
    const a=element('a',label); a.href=url;
    if (url.startsWith('https:')) { a.target='_blank'; a.rel='noopener noreferrer'; }
    return a;
  }
  function notify(message) {
    $('notice').textContent=message; $('notice').style.display='block';
    clearTimeout(notify.timer); notify.timer=setTimeout(() => { $('notice').style.display='none'; },2800);
  }
  for (const [id,title] of Object.entries(catalog.sessions)) {
    const opt=element('option',`${id} · ${title}`); opt.value=id; $('session').append(opt);
  }
  for (const family of [...new Set(projects.map(p => p.family))].sort()) {
    const opt=element('option',family); opt.value=family; $('family').append(opt);
  }
  function renderCards() {
    const query=$('search').value.toLocaleLowerCase().trim();
    const terms=query.split(/\s+/).filter(Boolean);
    const visible=projects.filter(p => {
      const haystack=[p.id,p.name,p.title,p.question,p.model,p.family,p.data].join(' ').toLocaleLowerCase();
      return terms.every(term => haystack.includes(term)) &&
        (!$('session').value || p.session===$('session').value) &&
        (!$('family').value || p.family===$('family').value) &&
        (!$('saved-only').checked || saved.has(p.id));
    });
    $('count').textContent=`${visible.length} of 118 projects`;
    const fragment=document.createDocumentFragment();
    for (const p of visible) {
      const card=element('button',undefined,'project-card'+(p.id===selected.id?' active':''));
      card.type='button'; card.setAttribute('aria-pressed',String(p.id===selected.id));
      card.append(element('span',`${p.id} / SESSION ${p.session} / ${p.family.toUpperCase()}`,'meta'),element('h3',p.name),element('p',p.title));
      const badges=element('div',undefined,'badges');
      badges.append(element('span',p.demo?'REFERENCE DEMO':'FORMAL SPECIFICATION','badge'));
      if(saved.has(p.id)) badges.append(element('span','SAVED','badge'));
      card.append(badges); card.addEventListener('click',()=>select(p)); fragment.append(card);
    }
    if (!visible.length) fragment.append(element('p','No matching projects. Reset filters or adjust your search.','empty'));
    $('cards').replaceChildren(fragment);
  }
  function section(title,text,className) {
    const frag=document.createDocumentFragment(); frag.append(element('h4',title),element('p',text,className)); return frag;
  }
  function renderDetail() {
    const p=selected; const box=$('detail'); box.replaceChildren();
    box.append(element('p',`${p.id} / ${catalog.sessions[p.session]}`,'eyebrow'),element('h3',p.name),element('p',p.title,'original'));
    box.append(element('p','PROPOSED RESEARCH MODEL · NO MEASUREMENTS INGESTED','source-state'));
    const actions=element('div',undefined,'actions');
    const save=element('button',saved.has(p.id)?'Unsave project':'Save project'); save.type='button'; save.setAttribute('aria-pressed',String(saved.has(p.id)));
    save.addEventListener('click',()=>{
      saved.has(p.id)?saved.delete(p.id):saved.add(p.id);
      try {localStorage.setItem('astra-saved-v1',JSON.stringify([...saved]));} catch (_) {notify('Saved for this session; browser storage unavailable.');}
      renderCards();renderDetail();
    });
    const compare=element('button',compared.includes(p.id)?'Remove comparison':'Compare project'); compare.type='button';
    compare.addEventListener('click',()=>{
      if(compared.includes(p.id)) compared=compared.filter(id=>id!==p.id);
      else if(compared.length<2) compared.push(p.id);
      else {notify('Clear one comparison before adding another project.');return;}
      renderComparison();renderDetail();
    });
    actions.append(save,compare,link('Full dossier',`../${p.dossier}`)); box.append(actions);
    box.append(section('Scientific question',p.question),section('Governing model',p.model,'equation'),section('Required observations & metadata',p.data),section('Validation & falsification',p.validation));
    const img=document.createElement('img');img.src=`../${p.workflow}`;img.alt=`${p.name}: conceptual research architecture, no measured results`;img.loading='lazy';box.append(img);
    box.append(section('Science visual to build',p.visual),section('Ambitious extension',p.extension));
    if(p.demo) {
      box.append(section('Executable reference',demos[p.demo].limitations));
      box.append(link('Inspect synthetic reference JSON',`../data/synthetic/${p.demo}.json`));
      if([...$('demo').options].some(o=>o.value===p.demo)) {
        const button=element('button','Open relevant model view');button.type='button';
        button.addEventListener('click',()=>{$('demo').value=p.demo;syncLab();$('laboratory').scrollIntoView({block:'start'});});box.append(button);
      }
    } else box.append(section('Implementation state','Project-specific scientific solver pending. The dossier supplies a model and validation plan, not fabricated numerical output.'));
    if(p.related.length) {
      box.append(element('h4','Connected projects'));const related=element('div',undefined,'related');
      for(const id of p.related) {const button=element('button',`${id} · ${byId.get(id).name}`);button.type='button';button.addEventListener('click',()=>select(byId.get(id)));related.append(button);}box.append(related);
    }
    box.append(element('h4','Original project provenance'),link(`2021 symposium / ${p.original_locator}`,p.provenance_url));
    box.append(element('h4','Resources & citation scope'));
    const list=element('ul',undefined,'resource-list');
    for(const id of p.sources) {
      const s=sources.get(id),li=element('li');li.append(link(s.title,s.url),element('small',`${s.status.toUpperCase()} · ${s.role}`),element('small',s.limitations));list.append(li);
    }box.append(list);
  }
  function select(p) {
    selected=p;history.replaceState(null,'',`#${p.id}`);renderCards();renderDetail();
    if(matchMedia('(max-width:760px)').matches)$('detail').scrollIntoView({block:'start'});
  }
  function renderComparison() {
    $('comparison').hidden=compared.length===0;
    const grid=$('compare-grid');grid.replaceChildren();
    for(const id of compared){const p=byId.get(id),col=element('article');col.append(element('h3',`${id} · ${p.name}`),element('p',p.title),section('Question',p.question),section('Model',p.model),section('Independent check',p.validation),section('Required data',p.data));grid.append(col);}
    if(compared.length===1)grid.append(element('p','Select a second project and choose Compare project.'));
  }
  $('clear-compare').addEventListener('click',()=>{compared=[];renderComparison();renderDetail();});
  $('filters').addEventListener('submit',event=>event.preventDefault());
  for(const id of ['search','session','family','saved-only'])$(id).addEventListener('input',renderCards);
  $('reset').addEventListener('click',()=>{$('filters').reset();renderCards();});
  document.addEventListener('keydown',event=>{
    if(event.key==='/'&&!['INPUT','SELECT','TEXTAREA'].includes(document.activeElement.tagName)){event.preventDefault();$('search').focus();}
    if(event.key==='Escape'&&document.activeElement===$('search')){$('search').value='';renderCards();}
  });
  for(const source of catalog.sources){const card=element('article',undefined,'source-card');card.append(element('p',`${source.id} / ${source.status}`,'source-state'+(source.status==='blocked'?' blocked':'')),link(source.title,source.url),element('p',source.role),element('p',source.limitations));$('source-grid').append(card);}

  // Educational visualizations use local deterministic reference data only.
  const canvas=$('canvas'),ctx=canvas.getContext('2d');
  let width=1000,height=500,angle=0.6;
  function resize(){const rect=canvas.getBoundingClientRect(),scale=Math.min(devicePixelRatio||1,2);width=rect.width;height=rect.height;canvas.width=Math.round(width*scale);canvas.height=Math.round(height*scale);ctx.setTransform(scale,0,0,scale,0,0);draw();}
  function text(value,x,y,color='#9db5d0',size=11){ctx.fillStyle=color;ctx.font=`${size}px ui-monospace,monospace`;ctx.fillText(value,x,y);}
  function chart(data,xIndex,yIndices,labels,{logX=false,equal=false}={}) {
    const left=62,right=width-25,top=58,bottom=height-60;
    let xs=data.rows.map(r=>logX?Math.log10(r[xIndex]):r[xIndex]);
    const values=data.rows.flatMap(r=>yIndices.map(i=>r[i]));
    let xl=Math.min(...xs),xh=Math.max(...xs),yl=Math.min(...values),yh=Math.max(...values);
    if(equal){const scale=Math.max((xh-xl)/(right-left),(yh-yl)/(bottom-top))*1.1;const xm=(xl+xh)/2,ym=(yl+yh)/2;const xspan=scale*(right-left),yspan=scale*(bottom-top);xl=xm-xspan/2;xh=xm+xspan/2;yl=ym-yspan/2;yh=ym+yspan/2;}
    else {const pad=(yh-yl||1)*.07;yl-=pad;yh+=pad;}
    ctx.strokeStyle='#1e354f';ctx.lineWidth=1;
    for(let i=0;i<=4;i++){const y=top+(bottom-top)*i/4;ctx.beginPath();ctx.moveTo(left,y);ctx.lineTo(right,y);ctx.stroke();text((yh-(yh-yl)*i/4).toPrecision(3),5,y+4);}
    for(let i=0;i<=4;i++){const x=left+(right-left)*i/4;const value=xl+(xh-xl)*i/4;text(value.toPrecision(3),x-10,bottom+20);}
    const colors=['#6bdde8','#b7a4fa','#efcf8a'];
    yIndices.forEach((index,k)=>{ctx.beginPath();data.rows.forEach((row,i)=>{const x=left+(right-left)*(xs[i]-xl)/(xh-xl||1);const y=bottom-(bottom-top)*(row[index]-yl)/(yh-yl||1);i?ctx.lineTo(x,y):ctx.moveTo(x,y);});ctx.strokeStyle=colors[k%3];ctx.lineWidth=1.8;ctx.stroke();text(labels[k],left+k*Math.min(230,width/3),32,colors[k%3]);});
    text((logX?'log10 ':'')+data.columns[xIndex],left,bottom+43);
  }
  function project3D(point){const c=Math.cos(angle),s=Math.sin(angle),tilt=.4;let [x,y,z]=point;const rx=c*x+s*z,rz=-s*x+c*z;const ry=Math.cos(tilt)*y-Math.sin(tilt)*rz;const depth=Math.sin(tilt)*y+Math.cos(tilt)*rz;const scale=Math.min(width,height)*.21/(1+depth*.11);return [width/2+rx*scale,height/2-ry*scale];}
  function cubePart(y,halfWidth,halfHeight,color){
    const vertices=[];for(const yy of [y-halfHeight,y+halfHeight])for(const z of [-halfWidth,halfWidth])for(const x of [-halfWidth,halfWidth])vertices.push(project3D([x,yy,z]));
    ctx.strokeStyle=color;ctx.lineWidth=1.5;
    for(const [a,b] of [[0,1],[1,3],[3,2],[2,0],[4,5],[5,7],[7,6],[6,4],[0,4],[1,5],[2,6],[3,7]]){ctx.beginPath();ctx.moveTo(...vertices[a]);ctx.lineTo(...vertices[b]);ctx.stroke();}
  }
  function cubesat(){text('EAGLESAT / EDUCATIONAL 3U SCHEMATIC',20,30,'#6bdde8');cubePart(0,.5,1.5,'#7b96b8');const explode=Number($('control').value)/100;for(let i=0;i<4;i++)cubePart(-1.05+i*.7+(i-1.5)*explode*.6,.44,.06,['#6bdde8','#b7a4fa','#efcf8a','#7cd5b2'][i]);text('Arrow keys rotate; slider separates illustrative subsystem decks',20,height-37);text('NOT TO SCALE / NO FLIGHT INTERFACES / NOT MANUFACTURER CAD',20,height-16,'#efcf8a',10);}
  function draw(){
    if(!ctx)return;ctx.clearRect(0,0,width,height);ctx.fillStyle='#050b16';ctx.fillRect(0,0,width,height);
    const mode=$('demo').value;if(mode==='cubesat'){cubesat();return;}
    const data=demos[mode];if(!data)return;
    if(mode==='fractal'){
      const cap=16+Math.round(Number($('control').value)*1.12);
      data.rows.forEach((r,i)=>{const n=r[2];const t=n&&n<=cap?Math.log1p(n)/Math.log1p(cap):0;ctx.fillStyle=t?`hsl(${190+t*85},65%,${18+t*45}%)`:'#080d1e';ctx.fillRect(32+(i%64)*(width-64)/64,45+Math.floor(i/64)*(height-95)/48,(width-64)/64+.2,(height-95)/48+.2);});
      text(`FINITE ESCAPE-TIME / DISPLAY CAP ${cap} / dark = unresolved at this cap`,20,25,'#6bdde8');text('real c: -2 to 1 / imaginary c: -1.2 to 1.2 / no proof of membership',20,height-15);
    } else if(mode==='orbit'){
      chart(data,1,[2],['two-body orbit (GM=a=1)'],{equal:true});
      const row=data.rows[Math.round(Number($('control').value)/100*(data.rows.length-1))];
      text(`t=${row[0].toFixed(3)} / E=${row[3].toFixed(6)} / angular momentum=${row[4].toFixed(6)}`,70,48,'#efcf8a');
    } else if(mode==='phase'){chart(data,0,[1,2],['ideal liquidus A (K)','ideal liquidus B (K)']);}
    else if(mode==='thermal'){chart(data,0,[1],['temperature (K)']);}
    else if(mode==='spectrum'){chart(data,0,[1,2],['truth relative flux','synthetic noisy flux']);}
    else if(mode==='radiation'){chart(data,0,[3],['synthetic count rate (1/s)']);}
    else if(mode==='attitude'){chart(data,0,[3],['single-axis attitude error (rad)']);}
  }
  function summary(data){
    const table=element('table'),thead=element('thead'),head=element('tr');
    data.columns.forEach(c=>head.append(element('th',c)));thead.append(head);table.append(thead);
    const body=element('tbody');
    const indexes=[0,Math.floor(data.rows.length/4),Math.floor(data.rows.length/2),Math.floor(3*data.rows.length/4),data.rows.length-1];
    for(const index of indexes){const row=element('tr');data.rows[index].forEach(v=>row.append(element('td',Number(v).toPrecision(5))));body.append(row);}table.append(body);
    $('data-summary').replaceChildren(element('p',`Five sampled rows of ${data.rows.length}. Full checked-in dataset available through export.`,'subtle'),table);
  }
  function syncLab(){
    const mode=$('demo').value;const interactive=['fractal','orbit','cubesat'].includes(mode);
    $('control-label').hidden=!interactive;
    const label=$('control-label');label.firstChild.textContent=mode==='cubesat'?'Subsystem separation':mode==='fractal'?'Display iteration cap':'Time sample';
    $('control-value').textContent=$('control').value+' / 100';
    $('export-demo').disabled=mode==='cubesat';
    if(mode==='cubesat'){
      $('lab-caption').textContent='Original educational 3U envelope and four generic subsystem decks. No dimensions, load qualification or flight interface compliance is implied.';
      $('data-summary').replaceChildren(element('p','This is conceptual geometry, not measured data. Arrow keys rotate the view; the slider separates decks.','subtle'));
    } else { $('lab-caption').textContent=demos[mode].limitations;summary(demos[mode]);}
    draw();
  }
  $('demo').addEventListener('change',syncLab);
  $('control').addEventListener('input',()=>{$('control-value').textContent=$('control').value+' / 100';draw();});
  canvas.addEventListener('keydown',event=>{if($('demo').value==='cubesat'&&['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();angle+=event.key==='ArrowRight'?.15:-.15;draw();}});
  let lastX=null;
  canvas.addEventListener('pointerdown',event=>{if($('demo').value==='cubesat'){lastX=event.clientX;canvas.setPointerCapture(event.pointerId);}});
  canvas.addEventListener('pointermove',event=>{if(lastX!==null){angle+=(event.clientX-lastX)*.008;lastX=event.clientX;draw();}});
  for(const ev of ['pointerup','pointercancel','lostpointercapture'])canvas.addEventListener(ev,()=>{lastX=null;});
  $('export-demo').addEventListener('click',()=>{
    const mode=$('demo').value;if(mode==='cubesat')return;
    const blob=new Blob([JSON.stringify(demos[mode],null,2)],{type:'application/json'}),url=URL.createObjectURL(blob);
    const a=link('',url);a.download=`astra-${mode}-SYNTHETIC.json`;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  new ResizeObserver(resize).observe(canvas);
  renderCards();renderDetail();syncLab();resize();
})();
