from django.core.management.base import BaseCommand
from tracker.models import Food


class Command(BaseCommand):
    help = 'Populate database with food items including Indian breakfast items'

    def handle(self, *args, **options):
        foods_data = [
            # Existing general foods
        
            {'name': 'Eggs', 'carbs': 0.6, 'protein': 13.0, 'fats': 11.0, 'calories': 155},
            {'name': 'Broccoli', 'carbs': 6.0, 'protein': 3.0, 'fats': 0.4, 'calories': 34},
            {'name': 'Spinach', 'carbs': 3.6, 'protein': 2.9, 'fats': 0.4, 'calories': 23},
            {'name': 'Oatmeal', 'carbs': 27.0, 'protein': 5.0, 'fats': 3.0, 'calories': 150},
            {'name': 'Almonds', 'carbs': 6.0, 'protein': 21.0, 'fats': 49.0, 'calories': 579},
            {'name': 'Cashew (Kaju)', 'carbs': 30.0, 'protein': 18.0, 'fats': 44.0, 'calories': 553},
            {'name': 'Groundnut (Peanut)', 'carbs': 16.0, 'protein': 26.0, 'fats': 49.0, 'calories': 567},
            {'name': 'Pistachio (Pista)', 'carbs': 28.0, 'protein': 20.0, 'fats': 45.0, 'calories': 562},
            {'name': 'Walnut (Akrod)', 'carbs': 14.0, 'protein': 15.0, 'fats': 65.0, 'calories': 654},
            {'name': 'Chana (Chickpeas, dry)', 'carbs': 61.0, 'protein': 19.0, 'fats': 6.0, 'calories': 364},
            {'name': 'Moong Dal (Green Gram)', 'carbs': 63.0, 'protein': 24.0, 'fats': 1.0, 'calories': 347},
            {'name': 'Black Moong', 'carbs': 59.0, 'protein': 24.0, 'fats': 1.5, 'calories': 341},          
            
            
            # Indian Breakfast Items
            {'name': 'Idli + Sambar', 'carbs': 32.0, 'protein': 6.0, 'fats': 2.0, 'calories': 180},
            {'name': 'Dosa (Plain)', 'carbs': 30.0, 'protein': 3.0, 'fats': 4.0, 'calories': 165},
            {'name': 'Masala Dosa', 'carbs': 45.0, 'protein': 8.0, 'fats': 8.0, 'calories': 300},
            {'name': 'Uttapam', 'carbs': 35.0, 'protein': 6.0, 'fats': 5.0, 'calories': 200},
            {'name': 'Poha', 'carbs': 40.0, 'protein': 4.0, 'fats': 4.0, 'calories': 200},
            {'name': 'Upma', 'carbs': 42.0, 'protein': 4.5, 'fats': 6.0, 'calories': 235},
            {'name': 'Vada', 'carbs': 18.0, 'protein': 3.0, 'fats': 7.0, 'calories': 150},
            {'name': 'Medu Vada (fried)', 'carbs': 20.0, 'protein': 3.5, 'fats': 8.0, 'calories': 170},
            {'name': 'Puri + Aloo Bhaji', 'carbs': 48.0, 'protein': 6.0, 'fats': 10.0, 'calories': 325},                     
            {'name': 'Sabudana Khichdi', 'carbs': 60.0, 'protein': 2.0, 'fats': 8.0, 'calories': 350},
            {'name': 'Dhokla', 'carbs': 12.0, 'protein': 3.0, 'fats': 1.5, 'calories': 85},
            {'name': 'Samosa', 'carbs': 32.0, 'protein': 6.0, 'fats': 17.0, 'calories': 262},
            {'name': 'Kachori', 'carbs': 35.0, 'protein': 7.0, 'fats': 20.0, 'calories': 300},
            
            # Bread & Bakery Items
            {'name': 'White Bread', 'carbs': 13.0, 'protein': 2.5, 'fats': 1.0, 'calories': 70},
            {'name': 'Brown Bread', 'carbs': 12.0, 'protein': 3.0, 'fats': 1.0, 'calories': 65},
            {'name': 'Butter', 'carbs': 0.0, 'protein': 0.1, 'fats': 4.0, 'calories': 35},
            {'name': 'Jam', 'carbs': 6.0, 'protein': 0.1, 'fats': 0.0, 'calories': 25},
            {'name': 'Peanut Butter (1 tbsp)', 'carbs': 3.0, 'protein': 4.0, 'fats': 8.0, 'calories': 95},                     
            {'name': 'Omelette (2 eggs)', 'carbs': 1.2, 'protein': 13.0, 'fats': 14.0, 'calories': 190},           
            
            
            # Dairy & Beverages
            {'name': 'Milk ', 'carbs': 12.0, 'protein': 8.0, 'fats': 3.0, 'calories': 120},
            {'name': 'Curd / Yogurt', 'carbs': 11.0, 'protein': 10.0, 'fats': 4.0, 'calories': 100},
            {'name': 'Lassi (sweet)', 'carbs': 35.0, 'protein': 8.0, 'fats': 5.0, 'calories': 220},
            {'name': 'Tea (with sugar)', 'carbs': 14.0, 'protein': 0.5, 'fats': 0.5, 'calories': 70},
            {'name': 'Tea (without sugar)', 'carbs': 1.0, 'protein': 0.5, 'fats': 0.2, 'calories': 5},
            {'name': 'Coffee (with sugar)', 'carbs': 18.0, 'protein': 0.5, 'fats': 1.0, 'calories': 90},
            {'name': 'Coffee (without sugar)', 'carbs': 1.0, 'protein': 0.5, 'fats': 0.2, 'calories': 5},
            
            # Fruits (updating/adding)
            {'name': 'Papaya', 'carbs': 13.0, 'protein': 0.5, 'fats': 0.2, 'calories': 55},
            {'name': 'Watermelon', 'carbs': 11.0, 'protein': 0.6, 'fats': 0.2, 'calories': 45},
            {'name': 'Guava', 'carbs': 14.0, 'protein': 2.5, 'fats': 1.0, 'calories': 65},
            {'name': 'Pomegranate', 'carbs': 21.0, 'protein': 1.7, 'fats': 1.2, 'calories': 105},
            {'name': 'Apple', 'carbs': 25.0, 'protein': 0.5, 'fats': 0.3, 'calories': 95},
            {'name': 'Banana', 'carbs': 27.0, 'protein': 1.3, 'fats': 0.4, 'calories': 105},
            {'name': 'Orange', 'carbs': 21.0, 'protein': 1.0, 'fats': 0.2, 'calories': 62},
            {'name': 'Mango', 'carbs': 25.0, 'protein': 1.0, 'fats': 0.4, 'calories': 99}, 
            {'name': 'Grapes', 'carbs': 18.0, 'protein': 0.7, 'fats': 0.2, 'calories': 69},
            
        ]

        created_count = 0
        updated_count = 0
        for food_data in foods_data:
            food, created = Food.objects.get_or_create(
                name=food_data['name'],
                defaults=food_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created food: {food.name}')
                )
            else:
                # Update existing food if it exists
                Food.objects.filter(name=food_data['name']).update(**food_data)
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated food: {food.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} food items.')
        )
        if updated_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'Updated {updated_count} existing food items.')
            )
