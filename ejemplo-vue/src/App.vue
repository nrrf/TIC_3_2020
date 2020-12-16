<template>
<div>
  <h1>Hola mundo en VueJS </h1>
  <hr/>
  <h1>{{message}}</h1>
  <button v-on:click="cambiar_mensaje">Cambio de estado</button>
  <hr/>
  <button v-on:click="contar">Es te boton se preciono {{count}} veces</button>
  <button v-on:click="reiniciar">Reiniciar contador</button>
  <hr/>
  <h1>{{input}}</h1>
  <input type="text" placeholder="texto" v-model="input">
  <br/>
  <h2>Imprimiendo lista</h2>
  <ul>
    <li v-for="(value,index) in users" v-bind:key="index">
      Nombre:{{value}}
    </li>
  </ul>
  <hr/>
  <h1 v-if="linterna">Encendido</h1>
  <h1 v-else>Apagado</h1>
  <button @click="cambiar_linterna">Cambio</button>
  </div>
</template> 

<script>
export default{
name : 'App', 
components:{},
data: function(){
  return{
    message: "Este es un nuevo mensaje",
    count:0, 
    input: "...", 
    users:["juan","maria","pablo","luisa"], 
    linterna: true
  }
},
methods:{
  cambiar_mensaje(){
    this.message="Este es otro mensaje"
  },
  contar(){
    this.count++
  }, 
  reiniciar(){
    this.count=0
  }, 
  cambiar_linterna(){
    this.linterna = !this.linterna
  }
}
}
</script>