const { createApp, ref } = Vue

  createApp({

    data() {
        return {
            title: "¡Bienvenido a Vue.js!",
            subtitle: "Lo mejor está por venir",
        }
    },
    
  }).mount('#app')