/* Offline interaction checks with a minimal DOM/canvas harness.
 * This verifies interaction logic; it is not a browser rendering test. */
'use strict';
const fs=require('fs'),vm=require('vm'),assert=require('assert');
class Node {
  constructor(tag='div'){this.tagName=tag.toUpperCase();this.children=[];this.listeners={};this.style={};this.attributes={};this.value='';this.checked=false;this.hidden=false;this.disabled=false;this._text='';}
  get textContent(){return this._text+this.children.map(c=>typeof c==='string'?c:c.textContent).join('');}
  set textContent(value){this._text=String(value);this.children=[];}
  append(...nodes){this.children.push(...nodes);}
  replaceChildren(...nodes){this._text='';this.children=[...nodes];}
  setAttribute(key,value){this.attributes[key]=value;}
  addEventListener(key,fn){(this.listeners[key]??=[]).push(fn);}
  dispatch(key,extra={}){for(const fn of this.listeners[key]||[])fn({preventDefault(){},...extra});}
  scrollIntoView(){}
  focus(){document.activeElement=this;}
  remove(){}
  click(){this.dispatch('click');}
  get options(){return this.children;}
  get firstChild(){return this.children[0];}
  reset(){for(const id of ['search','session','family'])nodes[id].value='';nodes['saved-only'].checked=false;}
  getBoundingClientRect(){return{width:900,height:430};}
  getContext(){return new Proxy({},{get:()=>()=>{}});}
  setPointerCapture(){}
}
const ids=['notice','session','family','search','saved-only','count','cards','detail','comparison','compare-grid','clear-compare','filters','reset','source-grid','canvas','demo','control','control-label','control-value','export-demo','lab-caption','data-summary','laboratory'];
const nodes=Object.fromEntries(ids.map(id=>[id,new Node()]));
nodes.search.tagName='INPUT';nodes.demo.tagName='SELECT';nodes.demo.value='fractal';nodes.control.value='35';
nodes['control-label'].children=[{textContent:'View angle'}];
for(const name of ['fractal','phase','orbit','thermal','spectrum','radiation','attitude','cubesat']){const opt=new Node('option');opt.value=name;nodes.demo.append(opt);}
const document={getElementById:id=>nodes[id],createElement:tag=>new Node(tag),createDocumentFragment:()=>new Node('fragment'),activeElement:new Node('body'),body:new Node('body'),addEventListener(){}};
const cache=new Map();
const context={document,window:{},console,location:{hash:''},history:{replaceState(){}},localStorage:{getItem:key=>cache.get(key)||null,setItem:(key,val)=>cache.set(key,val)},matchMedia:()=>({matches:false}),devicePixelRatio:1,ResizeObserver:class{constructor(fn){this.fn=fn;}observe(){this.fn();}},setTimeout:()=>1,clearTimeout(){},Blob,URL};
vm.createContext(context);
for(const file of ['catalog-data.js','model-data.js','app.js'])vm.runInContext(fs.readFileSync(`${__dirname}/../atlas/${file}`,'utf8'),context,{filename:file});
function flatten(n){return [n,...n.children.filter(c=>c instanceof Node).flatMap(flatten)];}
function cards(){return flatten(nodes.cards).filter(n=>String(n.className).includes('project-card'));}
function button(text){return flatten(nodes.detail).find(n=>n.tagName==='BUTTON'&&n.textContent===text);}
assert.equal(cards().length,118);assert(nodes.count.textContent.includes('118 of 118'));
nodes.search.value='Pseudomonas';nodes.search.dispatch('input');assert.equal(cards().length,1);cards()[0].click();assert(nodes.detail.textContent.includes('ISS MICROBIAL EVIDENCE'));
nodes.reset.click();assert.equal(cards().length,118);
nodes.session.value='I';nodes.session.dispatch('input');assert.equal(cards().length,13);
nodes.reset.click();cards()[0].click();button('Save project').click();nodes['saved-only'].checked=true;nodes['saved-only'].dispatch('input');assert.equal(cards().length,1);assert(cache.has('astra-saved-v1'));
nodes.reset.click();cards()[0].click();button('Compare project').click();cards()[1].click();button('Compare project').click();assert.equal(nodes['compare-grid'].children.length,2);assert.equal(nodes.comparison.hidden,false);
nodes['clear-compare'].click();assert.equal(nodes.comparison.hidden,true);
for(const mode of ['fractal','phase','orbit','thermal','spectrum','radiation','attitude','cubesat']){nodes.demo.value=mode;nodes.demo.dispatch('change');assert(nodes['lab-caption'].textContent.length>30);}
assert.equal(nodes['export-demo'].disabled,true);
nodes.canvas.dispatch('keydown',{key:'ArrowRight'});
assert.equal(nodes['source-grid'].children.length,51);
console.log('Atlas interaction checks passed: full inventory, filters, selection, saved list, comparison, eight model views, source states. Rendering not verified.');
