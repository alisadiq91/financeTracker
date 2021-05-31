$('.add-ingredient-list-item').click(function (event) {
    let ingredientItem = `<li class="list-item">
                                <div class="input-field">
                                    <i class="fas fa-times mr-4 remove-list-item"></i>
                                    <input name="ingredients1" id="ingredients1" type="text" maxlength="100" placeholder="Add ingredient..." required>
                                </div>
                          </li>`;      
                            
    $(this).parent().before(ingredientItem);
});

// Remove ingredient list item on click
$('#ingredients').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
});

$('.add-method-list-item').click(function (event) {
    let methodItem = `<li class="list-item">
                                <div class="input-field">
                                    <i class="fas fa-times mr-4 remove-list-item"></i>
                                    <input name="method1" id="method1" class="method-form" type="text" maxlength="100" placeholder="Add method step..." required>
                                </div>
                          </li>`;      
                            
    $(this).parent().before(methodItem);
});

// Remove ingredient list item on click
$('#method').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
});

$(function(){
    $(".logout-confirm").click(function(){
        if(confirm('Are you sure you want to logout?')) {
            return true;
        }

        return false;
    });
});

$(function(){
    $('.delete-confirm').click(function(){
        if(confirm('Are you sure you want to delete this recipe?')) {
            return true;
        }

        return false;
    });
});