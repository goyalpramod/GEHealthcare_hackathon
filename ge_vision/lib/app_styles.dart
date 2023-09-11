import 'package:flutter/material.dart';
import 'size_configs.dart';

Color kPrimaryColor = Color(0xff5C0FD1);
Color kSecondaryColor = Color(0xffA084CA);

final kTitle = TextStyle(
  fontFamily: ' SF Pro Text',
  fontSize: SizeConfig.blockSizeH! * 7,
  color: kPrimaryColor,
  fontWeight: FontWeight.w700,
);
final kBodyText1 = TextStyle(
  color: kSecondaryColor,
  fontSize: SizeConfig.blockSizeH! * 5.0,
  fontWeight: FontWeight.bold,
);
