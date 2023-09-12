class Category {
  int id;
  String name;
  String icon;

  Category({required this.id, required this.name, required this.icon});
}

List<Category> demoCategories = [
  Category(id: 1, name: 'Overall Body', icon: 'assets/images/Overall.png'),
  Category(id: 2, name: 'Skeletal System', icon: 'assets/images/skeleton.png'),
  Category(id: 3, name: 'Cardiovascular System', icon: 'assets/images/heart.png'),
  Category(id: 4, name: 'Neural System', icon: 'assets/images/brain.png'),
  Category(id: 5, name: 'Overall Body', icon: 'assets/images/Overall.png'),
  Category(id: 6, name: 'Skeletal System', icon: 'assets/images/skeleton.png'),
  Category(id: 7, name: 'Cardiovascular System', icon: 'assets/images/heart.png'),
  Category(id: 8, name: 'Neural System', icon: 'assets/images/brain.png'),
];
