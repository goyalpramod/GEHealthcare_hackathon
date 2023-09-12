import 'package:flutter/material.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:ge_vision/size_configs.dart';

class OnBoardBtn extends StatelessWidget {
  const OnBoardBtn({
    Key? key,
    required this.name,
    required this.onPressed,
    required this.backgroundColor, required this.textColor,
  }) : super(key: key);

  final String name;
  final VoidCallback onPressed;
  final Color backgroundColor;
  final Color textColor;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onPressed,
      borderRadius: BorderRadius.circular(6),
      child: Container(
        decoration: BoxDecoration(
          color: backgroundColor,
          borderRadius: BorderRadius.circular(6),
        ),
        padding: const EdgeInsets.fromLTRB(12.0, 10.0, 12.0, 10.0),
        child: Center(
          child: Text(
            name,
            style: TextStyle(
              color: textColor,
              fontSize: SizeConfig.blockSizeH! * 4.0,
              fontWeight: FontWeight.w600
            ),
          ),
        ),
      ),
    );
  }
}
