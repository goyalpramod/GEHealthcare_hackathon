import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:ge_vision/size_configs.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

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
          height: SizeConfig.blockSizeH! * 14, // Decrease the height to make it smaller
        ),
        centerTitle: true,
        leading: Transform.translate(
          offset: Offset(SizeConfig.defaultPaddingSize * 0.2, 0),
          child: Container(
            height: SizeConfig.blockSizeH! * 3,
            width: SizeConfig.blockSizeH! * 3, // Increase the width to make it larger
            decoration: BoxDecoration(
              border: Border.all(color: kPrimaryColor, width: 1),
              borderRadius: BorderRadius.circular(10),
            ),
            child: IconButton(
              icon: Icon(LineAwesomeIcons.arrow_right, color: kPrimaryColor),
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
          mainAxisAlignment: MainAxisAlignment.spaceBetween, // Align icons at the ends
          children: [
            Navitem(icon: Icon(LineAwesomeIcons.star)),
            Container(
              padding: EdgeInsets.all(8), // Add padding to the container
              decoration: BoxDecoration(
                color: kSecondaryColor.withOpacity(0.3), // Set the background color
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(LineAwesomeIcons.home, color: kPrimaryColor), // Set the color of the icon
            ),
            
            Navitem(icon: Icon(LineAwesomeIcons.cog)),
          ],
        ),
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(SizeConfig.defaultPaddingSize),
        child: SafeArea(child: Column(
          children: [
            TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(15))
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(15))
                ),
                fillColor: kSecondaryColor.withOpacity(0.3),
                filled: true,
                contentPadding: EdgeInsets.symmetric(horizontal: SizeConfig.defaultPaddingSize),
                prefixIcon: Icon(LineAwesomeIcons.search),
                hintText: 'Find the anatomy you desire'
              ),
            )
          ],
        )),
      ),
    );
  }
}

class Navitem extends StatelessWidget {
  const Navitem({
    super.key,
    required this.icon,
  });

  final Icon icon;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {},
      child: icon,
    );
  }
}
