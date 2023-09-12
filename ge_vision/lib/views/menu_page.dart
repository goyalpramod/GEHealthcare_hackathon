import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:ge_vision/model/category.dart';
import 'package:ge_vision/size_configs.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:ge_vision/views/detail_page.dart';

class MenuPage extends StatelessWidget {
  const MenuPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        title: Image.asset(
          'assets/images/LOGOi.png',
          height: SizeConfig.blockSizeH! * 14,
        ),
        centerTitle: true,
        leading: Transform.translate(
          offset: Offset(SizeConfig.defaultPaddingSize * 0.2, 0),
          child: Container(
            height: SizeConfig.blockSizeH! * 3,
            width: SizeConfig.blockSizeH! * 3,
            child: IconButton(
              icon: Icon(Icons.arrow_back_ios, color: kPrimaryColor),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
          ),
        ),
        actions: [
          Container(
            child: IconButton(
              icon: Icon(LineAwesomeIcons.user_circle, color: kPrimaryColor),
              onPressed: () {},
            ),
          ),
        ],
        systemOverlayStyle: SystemUiOverlayStyle.light,
      ),
      bottomNavigationBar: Container(
        height: SizeConfig.blockSizeH! * 10,
        width: double.infinity,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(25),
        ),
        margin: EdgeInsets.all(SizeConfig.defaultPaddingSize),
        padding: EdgeInsets.symmetric(
          horizontal: SizeConfig.defaultPaddingSize * 1.5,
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            NavItem(icon: Icon(LineAwesomeIcons.star)),
            Container(
              padding: EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: kSecondaryColor.withOpacity(0.3),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Expanded(
                child: Icon(LineAwesomeIcons.home, color: kPrimaryColor),
              ),
            ),
            NavItem(icon: Icon(LineAwesomeIcons.cog)),
          ],
        ),
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(SizeConfig.defaultPaddingSize),
        child: SafeArea(
          child: Column(
            children: [
              TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(15)),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(15)),
                    borderSide: BorderSide(color: kPrimaryColor),
                  ),
                  fillColor: kSecondaryColor.withOpacity(0.3),
                  filled: true,
                  contentPadding:
                      EdgeInsets.symmetric(horizontal: SizeConfig.defaultPaddingSize),
                  prefixIcon: Icon(LineAwesomeIcons.search),
                  hintText: 'Find the anatomy you desire',
                ),
              ),
              SizedBox(height: SizeConfig.blockSizeH! * 6),
              GridView.builder(
                shrinkWrap: true,
                physics: NeverScrollableScrollPhysics(),
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2, 
                  childAspectRatio: 0.95,
                ),
                itemCount: demoCategories.length,
                itemBuilder: (context, index) {
                  final category = demoCategories[index];
                  return CategoryCard(category: category);
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class NavItem extends StatelessWidget {
  const NavItem({
    Key? key,
    required this.icon
  }) : super(key: key);

  final Icon icon;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {},
      child: icon,
    );
  }
}

class CategoryCard extends StatelessWidget {
  final Category category;

  const CategoryCard({
    Key? key,
    required this.category,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => DetailPage(category: category)),
        );
      },
      child: Card(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(30),
        ),
        child: Stack(
          alignment: Alignment.bottomCenter,
          children: [
            Image.asset(
              category.icon,
              width: double.infinity,
              fit: BoxFit.cover, 
            ),
            Container(
              padding: EdgeInsets.all(SizeConfig.defaultPaddingSize),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(15),
                  bottomRight: Radius.circular(15),
                ),
              ),
              alignment: Alignment.bottomCenter,
              child: Text(
                category.name,
                style: TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
