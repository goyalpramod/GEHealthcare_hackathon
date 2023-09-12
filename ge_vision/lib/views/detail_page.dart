import 'package:flutter/material.dart';
import 'package:ge_vision/model/category.dart';
import 'package:ge_vision/size_configs.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class DetailPage extends StatefulWidget {
  final Category category;

  const DetailPage({
    Key? key,
    required this.category,
  }) : super(key: key);

  @override
  _DetailPageState createState() => _DetailPageState();
}

class _DetailPageState extends State<DetailPage> {
  int selectedGroup = -1; 

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
      ),
      body: Column(
        children: [
          Container(
            height: SizeConfig.blockSizeH! * 12,
            width: double.infinity,
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
            ),
            padding: EdgeInsets.symmetric(
              horizontal: SizeConfig.defaultPaddingSize * 1.5,
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween, 
              children: [
                buildNavItem(
                  icon: LineAwesomeIcons.bookmark,
                  label: 'Label',
                  index: 0,
                ),
                buildNavItem(
                  icon: LineAwesomeIcons.check,
                  label: 'Mark',
                  index: 1,
                ),
                buildNavItem(
                  icon: LineAwesomeIcons.file,
                  label: 'Export',
                  index: 2,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget buildNavItem({
    required IconData icon,
    required String label,
    required int index,
  }) {
    final isSelected = selectedGroup == index;

    return GestureDetector(
      onTap: () {
        
        setState(() {
          selectedGroup = index; 
        });
      },
      child: Container(
        padding: EdgeInsets.all(10), 
        decoration: BoxDecoration(
          color: isSelected ? kPrimaryColor : Colors.white, 
          borderRadius: BorderRadius.circular(10), 
        ),
        child: Row(
          children: [
            Icon(
              icon,
              color: isSelected ? Colors.white : Color.fromARGB(255, 64, 64, 64),
            ),
            SizedBox(width: 8), 
            Text(
              label,
              style: TextStyle(
                fontSize: 12, 
                color: isSelected ? Colors.white : Color.fromARGB(255, 64, 64, 64),
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
