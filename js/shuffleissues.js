    function shuffleissues() {
        $('.shuffleissues').each(function(idx, elem){
            var parent = $(elem);
        var divs = parent.children();
        while (divs.length) {
            parent.append(divs.splice(Math.floor(Math.random() * divs.length), 1)[0]);
        }
});
}
$( document ).ready(shuffleissues);
