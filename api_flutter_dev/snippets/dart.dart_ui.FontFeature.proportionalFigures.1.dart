import 'dart:ui';

import 'package:flutter/widgets.dart';

/// Flutter code sample for [FontFeature.FontFeature.proportionalFigures].

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
    // The Kufam font can be downloaded from Google Fonts
    // (https://www.google.com/fonts).
    return const Text(
      'Call 311-555-2368 now!',
      style: TextStyle(
        fontFamily: 'Kufam',
        fontFeatures: <FontFeature>[
          FontFeature.proportionalFigures(),
        ],
      ),
    );
  }
}
