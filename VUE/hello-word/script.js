const { createApp } = Vue
createApp({
    data() {
        return {
            // La directiva v-html cambia el innerHTML
            title: '<h1 class="title">¡Hola Mundo con Vue JS!</h1>',
            // La doble llave {{}} o el v-text cambian el textContext
            course: 'Codo a Codo',
            // Las directivas v-bind enlazan a atributos del HTML
            vueUrl: 'https://vuejs.org/',
            vueWebsite: 'vue-website',
            // Directiva v-for sirve para llenar una lista a través de un array
            fruits: [
                { name: "naranja", quantity: 10 },
                { name: "banana", quantity: 0 },
                { name: "durazno", quantity: 3 },
                { name: "pera", quantity: 0 }
            ],
            // Directiva v-model vincula el valor de los elementos HTML a los datos de la aplicación
            message: "Aquí va tu mensaje",
            counter: 0
        }
    }
}).mount('#app')  // el #app es el div con el id donde se enlaza VUE