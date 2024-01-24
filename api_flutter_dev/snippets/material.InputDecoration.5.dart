import 'package:flutter/material.dart';

/// Flutter code sample for [InputDecoration].

void main() => runApp(const MaterialStateExampleApp());

class MaterialStateExampleApp extends StatelessWidget {
  const MaterialStateExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text('InputDecoration Sample')),
        body: const MaterialStateExample(),
      ),
    );
  }
}

class MaterialStateExample extends StatelessWidget {
  const MaterialStateExample({super.key});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      initialValue: 'abc',
      decoration: InputDecoration(
        prefixIcon: const Icon(Icons.person),
        prefixIconColor:
            MaterialStateColor.resolveWith((Set<MaterialState> states) {
          if (states.contains(MaterialState.focused)) {
            return Colors.green;
          }
          if (states.contains(MaterialState.error)) {
            return Colors.red;
          }
          return Colors.grey;
        }),
      ),
    );
  }
}