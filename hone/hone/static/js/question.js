function QuestionCtrl($scope) {

    $scope.toggleCorrect = function() {

    }

}

$(function() {

    var getId = function($button) {
        return $button.siblings()[0].id.replace(/[^\d]/g, '');
    };

    var markCorrect = function($button, id) {
        var $correct = $("#id_answer_set-" + id + "-correct");
        $button.removeClass('btn-danger').addClass('btn-success');
        $button.val('Correct').text('Correct');
        $correct.val('True');
    };

    var markIncorrect = function($button, id) {
        var $correct = $("#id_answer_set-" + id + "-correct");
        $button.removeClass('btn-success').addClass('btn-danger');
        $button.val('Incorrect').text('Incorrect');
        $correct.val('False');
    };

    var getCorrect = function(id)
    {
        return $("#id_answer_set-" + id + "-correct");
    }

    var markAllIncorrect = function()
    {
        $('.correct-button').each(function(index, el) {
            markIncorrect($(el), index);
        });
    };

    var init = function()
    {
        var hasCorrect = false;
        $('.correct-button').each(function(index, el) {
            var $correct = getCorrect(index);
            if ($correct.val() === 'True') {
                hasCorrect = true;
                markCorrect($(el), index);
            }
        });

        if (!hasCorrect) {
            var $button = $('.correct-button')[0];
            markCorrect($button, 0);
        }
    }

    init();

    $('.correct-button').on('click', function() {
        var $button = $(this);
        var id = getId($button);
        var $correct = $("#id_answer_set-" + id + "-correct");
        var isCorrect = $correct.val() === 'True';

        // Toggle
        if (isCorrect) {
            markIncorrect($button, id);
        } else {
            markAllIncorrect();
            markCorrect($button, id);
        }
            
    });

    $('#id_question').on('keyup', function() {
        $('#questionPreview').html($(this).val());
    });

});
