// JavaScript code for frontend interactions

// Function to handle image deletion
function deleteImage(imageId) {
    fetch(`/images/delete/${imageId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to delete image');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        // Optionally, update image list after successful deletion
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
}

// Add event listener for delete button click
document.getElementById('confirmDelete').addEventListener('click', function() {
    const imageId = // Get the ID of the image to be deleted (you need to implement this)
    deleteImage(imageId);
});

// Add any other JavaScript interactions as needed

// Custom JavaScript for image carousel
$('.carousel').carousel({
    interval: 5000 // Adjust carousel interval
});
