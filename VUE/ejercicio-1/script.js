const { createApp, ref } = Vue

createApp({

  data() {
    return {
      title: "¡Bienvenido a Vue.js!",
      subtitle: "Lo mejor está por venir",
    }
  },

}).mount('#header')


createApp({

  data() {
    return {
      teal_paragraph: "<p class='teal-paragraph'>Este párrafo se generó con la directiva v-hmtl.</p>",
      url: "https://vuejs.org/",
      url_class: "vue-url",
      login: true,
    }
  },

}).mount("#main")


createApp({

  data() {
    return {
      developer: "Evan You",
      year: "2014",
    }
  },

}).mount("#footer")


createApp({

  data() {
    return {
      name: "Agustín",
      lastName: "Comolli",
      age: 46
    }
  },

  methods: {
    details() {
      return `${this.name} ${this.lastName} tiene ${this.age} años.`
    }
  },

}).mount("#my-card")


const myTitle = {
  template: "<h2 class='my-title'>{{ title }}</h2>",
  data() {
    return {
      title: "Mi primer componente",
    }
  },
};


const vueComponent = Vue.createApp({
  components: {
    "my-title": myTitle,
  }
}).mount("#vue-component");