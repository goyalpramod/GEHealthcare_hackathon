import 'package:flutter/material.dart';
import 'package:ge_vision/views/menu_page.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ge_vision/app_styles.dart';
import 'package:ge_vision/main.dart';
import 'package:ge_vision/model/onboard_data.dart';
import 'package:ge_vision/size_configs.dart';
import 'package:shared_preferences/shared_preferences.dart';
import './pages.dart';
import '../widgets/widgets.dart';

class OnBoardingPage extends StatefulWidget {
  const OnBoardingPage({Key? key}) : super(key: key);

  @override
  State<OnBoardingPage> createState() => _OnBoardingPageState();
}

class _OnBoardingPageState extends State<OnBoardingPage> {
  int currentPage = 0;

  PageController _pageController = PageController(initialPage: 0);

 AnimatedContainer dotIndicator(index) {
  return AnimatedContainer(
    margin: EdgeInsets.only(right: 5),
    duration: Duration(milliseconds: 400),
    height: 12,
    width: 12,
    decoration: BoxDecoration(
      color: currentPage == index ? kPrimaryColor : kSecondaryColor,
      borderRadius: BorderRadius.circular(6),
    ),
  );
}

  @override
  Widget build(BuildContext context) {
    SizeConfig().init(context);
    double sizeH = SizeConfig.blockSizeH!;
    double sizeV = SizeConfig.blockSizeV!;
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              flex: 9,
              child: PageView.builder(
                controller: _pageController,
                onPageChanged: (value) {
                  setState(() {
                    currentPage = value;
                  });
                },
                itemCount: onboardingContents.length,
                itemBuilder: (context, index) => Column(
                  children: [
                    SizedBox(
                      height: sizeV * 4,
                    ),
                    Padding(
                      padding: const EdgeInsets.only(left:12.0, right:12.0),
                      child: Text(
                        onboardingContents[index].title,
                        style: kTitle,
                        textAlign: TextAlign.center,
                      ),
                    ),
                    
                    Container(
                      height: sizeV * 50,
                      child: Image.asset(
                        onboardingContents[index].image,
                        fit: BoxFit.contain,
                      ),
                    ),
                    SizedBox(
                      height: sizeV * 3,
                    ),
                    Padding(
                      padding: const EdgeInsets.only(left:12.0, right:12.0),
                      child: RichText(
                        textAlign: TextAlign.center,
                        text: TextSpan(style: kBodyText1, children: [
                          TextSpan(text: 'Join '),
                          TextSpan(
                            text: 'GE',
                            style: TextStyle(
                              color: kPrimaryColor,
                            ),
                          ),
                          TextSpan(
                            text: 'Vision ',
                            style: TextStyle(
                              color: Colors.black,
                            ),
                          ),
                          TextSpan(text: 'to elevate your medical knowledge. Learn with unprecedented depth and clarity.'),
                        ]),
                      ),
                    ),
                    SizedBox(
                      height: sizeV * 4,
                    ),
                  ],
                ),
              ),
            ),
            Expanded(
              flex: 1,
              child: Column(
                children: [
                  currentPage == onboardingContents.length - 1
                      ? MyTextButton(
                          buttonName: 'Explore Anatomy',
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => MenuPage(),
                              ),
                            );
                          },
                          bgColor: kPrimaryColor,
                        )
                      : Row(
                          mainAxisAlignment: MainAxisAlignment.spaceAround,
                          children: [
                            OnBoardBtn(
                              name: 'Skip',
                              onPressed: () {},
                              backgroundColor: kPrimaryColor,
                            ),
                            Row(
                              children: List.generate(
                                onboardingContents.length,
                                (index) => dotIndicator(index),
                              ),
                            ),
                            OnBoardBtn(
                              name: 'Next',
                              onPressed: () {
                                _pageController.nextPage(
                                  duration: Duration(milliseconds: 400),
                                  curve: Curves.easeInOut,
                                );
                              },
                              backgroundColor: kPrimaryColor,
                            ),
                          ],
                        ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
