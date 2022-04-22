function Random() {
    var rnd = Math.floor(Math.random() * 1000000000);
    document.getElementById('id_slug').value = rnd;
}

var count_click = 2;

function count_click_add(){
    count_click +=1;
}

$("#count_click").text(count_click);

$( document ).ready(function(){
      $("button[name='count_click']").click(function(){
         count_click_add();
      });
});
