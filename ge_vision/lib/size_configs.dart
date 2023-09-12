import 'package:flutter/material.dart';

class SizeConfig {
  static MediaQueryData? _mediaQueryData;
  static double? screenWidth;
  static double? screenHeight;
  static double? blockSizeH;
  static double? blockSizeV;
  static double defaultPaddingPercentage = 6.0; // Adjust the percentage as needed

  void init(BuildContext context) {
    _mediaQueryData = MediaQuery.of(context);
    screenWidth = _mediaQueryData!.size.width;
    screenHeight = _mediaQueryData!.size.height;
    blockSizeH = screenWidth! / 100;
    blockSizeV = screenHeight! / 100;
  }

  // Calculate the default padding based on screen size
  static double get defaultPaddingSize {
    return screenWidth! * (defaultPaddingPercentage / 100.0);
  }
}
