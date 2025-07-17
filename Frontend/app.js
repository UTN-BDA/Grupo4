import React from 'react';
import { View, StyleSheet } from 'react-native';
import DatasheetView from './screens/DatasheetView';

export default function App() {
  return (
    <View style={styles.container}>
      <DatasheetView />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
