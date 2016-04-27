$('.list-view').each(->
    id = $(this).attr('id')
    Sortable.create(document.getElementById(id), {
        group: "list-view"
        animation: 150
        ghostClass: "ghost"  #  Class name for the drop placeholder
        chosenClass: "chosen"  #  Class name for the chosen item
    })
)
