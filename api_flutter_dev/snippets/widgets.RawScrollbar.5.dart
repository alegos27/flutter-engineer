import 'package:flutter/material.dart';

/// Flutter code sample for [RawScrollbar].

void main() => runApp(const RawScrollbarExampleApp());

class RawScrollbarExampleApp extends StatelessWidget {
  const RawScrollbarExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('RawScrollbar Sample')),
        body: const RawScrollbarExample(),
      ),
    );
  }
}

class RawScrollbarExample extends StatefulWidget {
  const RawScrollbarExample({super.key});

  @override
  State<RawScrollbarExample> createState() => _RawScrollbarExampleState();
}

class _RawScrollbarExampleState extends State<RawScrollbarExample> {
  final ScrollController _controllerOne = ScrollController();

  @override
  Widget build(BuildContext context) {
    return RawScrollbar(
      controller: _controllerOne,
      thumbVisibility: true,
      child: GridView.builder(
        controller: _controllerOne,
        itemCount: 120,
        gridDelegate:
            const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
        itemBuilder: (BuildContext context, int index) {
          return Center(
            child: Text('item $index'),
          );
        },
      ),
    );
  }
}
