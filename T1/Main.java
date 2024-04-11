import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    private char[][] mat;
    private int total, currDir, y, x;
    private Scanner in;
    private StringBuilder currNum;

    private Main() {
        in = new Scanner(System.in);
        currNum = new StringBuilder();
    }

    private void newTest(String path) throws FileNotFoundException {
        @SuppressWarnings("resource")
        Scanner reader = new Scanner(new File(path));
        String[] len = (reader.nextLine()).split(" ");
        int width, height;
        height = Integer.parseInt(len[0]);
        width = Integer.parseInt(len[1]);
        mat = new char[height][width];

        short lineNum = 0;
        while(reader.hasNext()) {
            String currLine = reader.nextLine();
            for(int i = 0; i < currLine.length(); i++) {
                mat[lineNum][i] = currLine.charAt(i);
            }
            lineNum++;
        }

        for(int i = 0; i < mat.length; i++) {
            if(mat[i][0] == '-') {
                y = i;
                break;
            }
        }
    }

    private void newNum() {
        if(Character.isDigit(mat[y][x])) {
            currNum.append(mat[y][x]);
        } else {
            if(currNum.length() > 0) {
            total += Integer.parseInt(currNum.toString());
            currNum.delete(0, currNum.length());
            }
        }

        return;
    }

    private int moveR() {
        char currPos = mat[y][x];
        newNum();
        switch(currPos) {
            case '/': y-=1; return 4;
            case '\\': y+=1; return 2;
        }
        x+=1;
        return 1;
    }

    private int moveL() {
        char currPos = mat[y][x];
        newNum();
        switch(currPos) {
            case '/': y+=1; return 2;
            case '\\': y-=1; return 4;
        }
        x-=1;
        return 3;
    }

    private int moveU() {
        char currPos = mat[y][x];
        newNum();
        switch(currPos) {
            case '/': x+=1; return 1;
            case '\\': x-=1; return 3;
        }
        y-=1;
        return 4;
    }

    private int moveD() {
        char currPos = mat[y][x];
        newNum();
        switch(currPos) {
            case '/': x-=1; return 3;
            case '\\': x+=1; return 1;
        }
        y+=1;
        return 2;
    }

    private void runTest() {
        x = 0;
        total = 0;
        currDir = 1;

        double start = System.nanoTime();

        while(mat[y][x] != '#') {
            switch(currDir) {
                case 1: currDir = moveR(); break;
                case 2: currDir = moveD(); break;
                case 3: currDir = moveL(); break;
                case 4: currDir = moveU(); break;
            }
        }

        newNum();

        double finish = System.nanoTime();

        System.out.println("The value " + total + " was found in " + (finish-start)/1000000000 + " seconds.\n");
    }

    private void runAllTests() throws FileNotFoundException {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        for(int i = 0; i <= 8; i++) {
            System.out.println("Case " + i + ":");
            String currTest = "Input" + i + ".txt";
            newTest(currTest);
            runTest();
        }
    }

    private void options() throws FileNotFoundException {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        System.out.println("Select test case:");
        System.out.println("0) exit\n1) 80x12\n2) 50x50\n3) 100x100\n4) 200x200\n5) 500x500\n6) 750x750\n7) 1000x1000\n8) 1500x1500\n9) 2000x2000\n10) Run all");

        int aux = in.nextInt();

        switch(aux) {
            case 0:
                return;
            case 10:
                runAllTests();
                return;
        }

        newTest("Input" + (aux-1) +".txt");
        runTest();

        System.out.println("\nEnter anything to test again.");
        in.next();
        options();
    }

    public static void main(String[] args) throws FileNotFoundException {
        Main menu = new Main();
        menu.options();
    }
}