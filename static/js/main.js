$(document).ready(function () {
    let isClicked = false
    $('select').click(function () {
        isClicked = !isClicked
        if (isClicked)
        // $(this).css('background', 'url("./assets/img/arrow_up.png") 100% / 5% no-repeat')
            $(this).addClass('arrow-up')
        else
        // $(this).css('background', 'url("./assets/img/arrow_down.png") 100% / 5% no-repeat')
            $(this).removeClass('arrow-up')
    })

    $('select').blur(function () {
        isClicked = false
        $(this).removeClass('arrow-up')
    })
})