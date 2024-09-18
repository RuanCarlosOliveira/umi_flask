const app = Vue.createApp({
    data() {
        return {
            expanded: false // Estado do menu (expandido ou colapsado)
        }
    },
    methods: {
        toggleMenu() {
            this.expanded = !this.expanded; // Alterna entre expandido e recolhido ao clicar
        }
    }
});

app.mount('#menu-app');
