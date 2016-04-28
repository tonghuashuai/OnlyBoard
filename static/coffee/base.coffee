$.extend({
    app: angular.module('app', ['ngRoute'])
    only_ajax: (option)->
        $.ajax({
            method: option.method,
            url: option.url,
            success: (r)->
                option.success(r)

            fail: ->
                foption.ail()
        })
})
