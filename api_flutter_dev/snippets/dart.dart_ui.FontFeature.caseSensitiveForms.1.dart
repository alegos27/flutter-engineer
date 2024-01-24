import 'dart:ui';

import 'package:flutter/widgets.dart';

/// Flutter code sample for [FontFeature.FontFeature.caseSensitiveForms].

void main() => runApp(const ExampleApp());

class ExampleApp extends StatelessWidget {
  const ExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return WidgetsApp(
      builder: (BuildContext context, Widget? navigator) =>
          const ExampleWidget(),
      color: const Color(0xffffffff),
    );
  }
}

class ExampleWidget extends StatelessWidget {
  const ExampleWidget({super.key});

  @override
  Widget build(BuildContext context) {
    // The Piazzolla font can be downloaded from Google Fonts
    // (https://www.google.com/fonts).
    return const Text(
      '(A) [A] {A} «A» A/B A•B',
      style: TextStyle(
        fontFamily: 'Piazzolla',
        fontFeatures: <FontFeature>[
          FontFeature.caseSensitiveForms(),
        ],
      ),
    );
  }
}