$('.list-view').each(->
    id = $(this).attr('id')
    Sortable.create(document.getElementById(id), {
        group: "list-view"
        animation: 150
        ghostClass: "ghost"  #  Class name for the drop placeholder
        chosenClass: "chosen"  #  Class name for the chosen item

        onUpdate: (event)->
            console.log event

        onAdd: (event)->
            console.log event
    })
)


$.app.controller('TaskCtrl', ($scope)->
    $scope.o = null
)


$.only_ajax({
    url: "/j/task/list",
    success: (r)->
        v = angular.element($("[ng-controller=TaskCtrl]")).scope()
        v.o = r.data
        v.$apply()
        false
})
