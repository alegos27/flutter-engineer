import 'package:flutter/material.dart';

/// Flutter code sample for [InputDecoration].

void main() => runApp(const InputDecorationExampleApp());

class InputDecorationExampleApp extends StatelessWidget {
  const InputDecorationExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text('InputDecoration Sample')),
        body: const InputDecorationExample(),
      ),
    );
  }
}

class InputDecorationExample extends StatelessWidget {
  const InputDecorationExample({super.key});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      initialValue: 'abc',
      decoration: const InputDecoration(
        prefix: Text('Prefix'),
        suffix: Text('Suffix'),
        border: OutlineInputBorder(),
      ),
    );
  }
}
