import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ge_vision/views/onboarding_page.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'GEVision',
      theme: ThemeData(
        textTheme: GoogleFonts.manropeTextTheme(
          Theme.of(context).textTheme,
        ),
      ),
      home: OnBoardingPage(),
    );
  }
}
