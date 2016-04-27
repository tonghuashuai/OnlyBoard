// Generated by CoffeeScript 1.4.0
(function() {

  $('.list-view').each(function() {
    var id;
    id = $(this).attr('id');
    return Sortable.create(document.getElementById(id), {
      group: "list-view",
      animation: 150,
      ghostClass: "ghost",
      chosenClass: "chosen",
      onUpdate: function(event) {
        return console.log(event);
      },
      onAdd: function(event) {
        return console.log(event);
      }
    });
  });

}).call(this);
