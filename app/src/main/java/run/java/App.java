package run.java;

import algorithms.Primes;
import algorithms.Sort;
import control.Double;
import control.Single;
import datastructures.DsVector;
import generator.GenVector;
import java.util.ArrayList;

public class App {
    public static void single() {
        System.out.println("SingleForLoop");
        System.out.println("-------------");
        System.out.println(String.format("SumRange(10): %s", Single.sumRange(10)));
        System.out.println(
                String.format("MaxArray([1, 2, 3, 4, 5]): %s",
                        Single.maxArray(new int[] { 1, 2, 3, 4, 5 })));
        System.out.println(
                String.format("SumModulus(100, 3): %s", Single.sumModulus(100, 3)));
        System.out.println();
    }

    public static void double_() {
        System.out.println("DoubleForLoop");
        System.out.println("-------------");
        System.out.println(
                String.format("SumSquare(10): %s", Double.sumSquare(10)));
        System.out.println(
                String.format("SumTriangle(10): %s", Double.sumTriangle(10)));
        System.out.println(
                String.format("CountPairs([1, 2, 3, 4, 5]): %s",
                        Double.countPairs(new int[] { 1, 2, 3, 4, 5, 2 })));
        System.out.println(
                String.format("CountDuplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]): %s",
                        Double.countDuplicates(new int[] { 1, 2, 3, 4, 5 },
                                new int[] { 1, 3, 2, 4, 5 })));
        System.out.println();
    }

    public static void vector() {
        ArrayList<Integer> inputVec = GenVector.generateVector(10, 10);
        ArrayList<Integer> inputVec2 = GenVector.generateVector(10, 10);

        System.out.println("Vector");
        System.out.println("------");
        System.out.println(
                String.format("ModifyVector(%s): %s", inputVec.toString(),
                        DsVector.modifyVector(inputVec).toString()));
        System.out.println(String.format("SearchVector(%s, 5): %s",
                inputVec.toString(),
                DsVector.searchVector(inputVec, 5)));
        System.out.println(String.format("SortVector(%s): %s", inputVec.toString(),
                DsVector.sortVector(inputVec).toString()));
        System.out.println(
                String.format("ReverseVector(%s): %s", inputVec.toString(),
                        DsVector.reverseVector(inputVec).toString()));
        System.out.println(
                String.format("RotateVector(%s, 3): %s", inputVec.toString(),
                        DsVector.rotateVector(inputVec, 3).toString()));
        System.out.println(String.format(
                "MergeVectors(%s, %s): %s", inputVec.toString(), inputVec2.toString(),
                DsVector.mergeVectors(inputVec, inputVec2).toString()));

        System.out.println();
    }

    public static void primes() {
        System.out.println("Primes");
        System.out.println("------");
        System.out.println(String.format("IsPrime(10): %s", Primes.isPrime(10)));
        System.out.println(
                String.format("SumPrimes(10): %s", Primes.sumPrimes(10)));
        System.out.println(String.format("PrimeFactors(10): %s",
                Primes.primeFactors(10).toString()));
        System.out.println();
    }

    public static void sort() {
        ArrayList<Integer> initialVec = GenVector.generateVector(20, 10);
        System.out.println("Sort");
        System.out.println("------");
        ArrayList<Integer> inputVec0 = new ArrayList<Integer>(initialVec);
        Sort.sortVector(inputVec0);
        System.out.println(String.format(
                "SortVector(%s): %s", initialVec.toString(), inputVec0.toString()));
        ArrayList<Integer> inputVec1 = new ArrayList<Integer>(initialVec);
        Sort.dutchFlagPartition(inputVec1, 5);
        System.out.println(String.format("DutchFlagPartition(%s, 5): %s",
                initialVec.toString(),
                inputVec1.toString()));
        System.out.println(String.format("MaxN(%s, 5): %s", initialVec.toString(),
                Sort.maxN(initialVec, 5).toString()));
        System.out.println();
    }

    public static void main(String[] args) {
        single();
        double_();
        vector();
        primes();
        sort();
    }
}
