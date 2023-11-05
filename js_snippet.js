// Function to clear the comment form
function clearForm() {
    document.getElementById("comment_form").reset();
}

// Add an event listener for the form submission
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("comment_form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission
        var form = event.target;
        var formData = new FormData(form);

        // Perform an AJAX request to submit the form data
        fetch(form.action, {
            method: form.method,
            body: formData
        })
        .then(function (response) {
            // Handle the response as needed
            // Display the success message
            var message = document.createElement('div');
            message.classList.add('alert', 'alert-success', 'mt-4');
            message.textContent = 'Your comment is awaiting approval';
            message.style.width = "50%"; // Set the width of the message here

            var formElement = document.getElementById("comment_form");
            formElement.parentNode.insertBefore(message, formElement.nextSibling);
            // Remove the message after 5 seconds
            setTimeout(function () {
                message.remove();
            }, 5000);
            clearForm(); // Clear the form fields
        })
        .catch(function (error) {
            // Handle any errors that occur during the submission
        });
    });
});