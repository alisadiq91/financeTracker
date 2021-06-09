// Add ingredient list item on click
$('.add-ingredient-list-item').click(function (event) {
    let ingredientItem = `<li class="list-item">
                                <div class="input-field">
                                    <a class="remove-list-item"><i class="fas fa-times mr-4 "></i></a>
                                    <input name="ingredients1" id="ingredients1" type="text" maxlength="100" placeholder="Add ingredient..." required>
                                </div>
                          </li>`;      
                            
    $(this).parent().after(ingredientItem);
});

// Remove ingredient list item on click
$("a.remove-list-item").on("click", function(event) {
console.log($(this));
console.log($(this).parent().parent());
});


// Add method step item on click
$('.add-method-list-item').click(function (event) {
    let methodItem = `<li class="list-item">
                                <div class="input-field">
                                    <i class="fas fa-times mr-4 remove-list-item"></i>
                                    <input name="method1" id="method1" class="method-form" type="text" maxlength="100" placeholder="Add method step..." required>
                                </div>
                          </li>`;      
                            
    $(this).parent().after(methodItem);
});

// Remove method step item on click
$('#method').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
});

// Function to confirm user wants to logout
$(function(){
    $(".logout-confirm").click(function(){
        if(confirm('Are you sure you want to logout?')) {
            return true;
        }

        return false;
    });
});

// Function to confirm user wants to delete recipe
$(function(){
    $('.delete-confirm').click(function(){
        if(confirm('Are you sure you want to delete this recipe?')) {
            return true;
        }

        return false;
    });
});