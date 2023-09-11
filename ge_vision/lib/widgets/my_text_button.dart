import 'package:flutter/material.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:ge_vision/size_configs.dart';

class MyTextButton extends StatelessWidget {
  const MyTextButton({
    Key? key,
    required this.buttonName,
    required this.onPressed,
    required this.bgColor,
  });
  final String buttonName;
  final VoidCallback onPressed;
  final Color bgColor;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      child: SizedBox(
        height: SizeConfig.blockSizeH! * 15.5,
        width: SizeConfig.blockSizeH! * 100,
        child: TextButton(
          onPressed: onPressed,
          child: Text(
            buttonName,
            style: TextStyle(
              color: Colors.white, 
              fontSize: SizeConfig.blockSizeH! * 5.0,
              fontWeight: FontWeight.bold,
            ),
          ),
          style: TextButton.styleFrom(
            backgroundColor: bgColor,
          ),
        ),
      ),
    );
  }
}
