let nutrientChart = null;

// Initialize Chart
function initializeChart(data) {
    const ctx = document.getElementById('nutrient-chart');
    if (!ctx) return;

    const total = data.carbs + data.protein + data.fats;
    
    if (total === 0) {
        // Show empty chart message
        ctx.parentElement.innerHTML = '<p style="text-align: center; color: #666;">No data to display. Add some food to see the breakdown!</p>';
        return;
    }

    const carbsPercent = ((data.carbs / total) * 100).toFixed(0);
    const proteinPercent = ((data.protein / total) * 100).toFixed(0);
    const fatsPercent = ((data.fats / total) * 100).toFixed(0);

    if (nutrientChart) {
        nutrientChart.destroy();
    }

    console.log('Initializing chart with data:', data);
    nutrientChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [`Carbs ${carbsPercent}%`, `Protein ${proteinPercent}%`, `Fats ${fatsPercent}%`],
            datasets: [{
                data: [data.carbs, data.protein, data.fats],
                backgroundColor: [                    
                    '#FFECD1',
                    '#FF7D00',
                    '#15616D',
                ],
                borderWidth: 2,
                borderColor: 'red',
                offset: [0, 0.1, 0]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: {
                            size: 14
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value.toFixed(1)}gm (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

// Add Food
document.addEventListener('DOMContentLoaded', function() {
    const addFoodBtn = document.getElementById('add-food-btn');
    const foodSearch = document.getElementById('food-search');
    const foodQuantity = document.getElementById('food-quantity');

    // Focus on food search input on page load
    if (foodSearch) {
        foodSearch.focus();
    }

    if (addFoodBtn && typeof foodsData !== 'undefined') {
        addFoodBtn.addEventListener('click', function() {
            const inputValue = foodSearch.value.trim();
            if (!inputValue) {
                alert('Please select a food item');
                return;
            }

            // Find food by name (case-insensitive)
            const foodName = Object.keys(foodsData).find(name =>
                name.toLowerCase() === inputValue.toLowerCase()
            );

            if (!foodName || !foodsData[foodName]) {
                alert('Food not found. Please select from the dropdown list.');
                return;
            }

            const foodId = foodsData[foodName].id;
            const quantity = parseFloat(foodQuantity.value) || 1;

            addFoodToConsumption(foodId, quantity);
        });
    }

    // Allow Enter key to add food
    if (foodSearch) {
        foodSearch.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                if (addFoodBtn) {
                    addFoodBtn.click();
                }
            }
        });
    }
});

function addFoodToConsumption(foodId, quantity) {
    fetch('/add-food/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            food_id: foodId,
            quantity: parseFloat(quantity)
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert(data.message || 'Error adding food');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error adding food');
    });
}

// Remove Food
function removeFood(consumptionId) {
    if (!confirm('Are you sure you want to remove this item?')) {
        return;
    }

    fetch(`/remove-food/${consumptionId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Error removing food');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error removing food');
    });
}

// Edit Goal Modal
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('goal-modal');
    const editBtn = document.getElementById('edit-goal-btn');
    const closeBtn = document.querySelector('.close');
    const saveBtn = document.getElementById('save-goal-btn');

    if (editBtn) {
        editBtn.addEventListener('click', function() {
            if (modal) modal.style.display = 'block';
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            if (modal) modal.style.display = 'none';
        });
    }

    if (saveBtn) {
        saveBtn.addEventListener('click', function() {
            const newGoal = document.getElementById('new-calorie-goal').value;
            updateCalorieGoal(newGoal);
        });
    }

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

function updateCalorieGoal(goal) {
    fetch('/update-goal/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            calorie_goal: parseInt(goal)
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Error updating calorie goal');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error updating calorie goal');
    });
}

// Get CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

