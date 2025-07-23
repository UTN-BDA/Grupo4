import React from 'react';
import { View, StyleSheet } from 'react-native';
import ViajesView from './screens/ViajesView';

export default function App() {
  return (
    <View style={styles.container}>
      <ViajesView/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
