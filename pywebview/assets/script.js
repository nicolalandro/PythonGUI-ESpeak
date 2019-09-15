window.app = new Vue({
  el: "#app",
  data: {
    message: 'body here'
  },
  methods: {
    change(){
         window.pywebview.api.changeMessage().then(
            (x) => { this.message = x['text'] } 
        )
    }
  }
});
