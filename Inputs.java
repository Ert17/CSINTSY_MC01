import java.util.*;

public class Inputs{

    public static void main(String[] args) {

        int i = 0;
        int k = 0;
        // Initial State: 1,1 position - 1,2 front
        int[][] miner = {{1,1}, {1,2}};
        int[] gold = new int[2];
        int[][] nBeacon = new int[64][64];
        int[][] nPit = new int[64][64];

        Scanner scan = new Scanner(System.in);

        /* ------------ INITIALIZATION --------------- */
        // grid size
        System.out.println("Enter Grid Size (n): ");
        int nSize = scan.nextInt(); // gridsize
        System.out.println("Grid size is: " + nSize + "\n");

        // gold coordinates
        System.out.println("Enter GOLD X coordinate: ");
        gold[0] = scan.nextInt();
        System.out.println("Enter GOLD Y coordinate: ");
        gold[1] = scan.nextInt();

        System.out.println("Gold coordinate is: ");
        for (i=0; i<2; i++)
          System.out.println(gold[i]);

        // pit and beacon computation and coordinates
        int pitval = (int)(Math.round(nSize * 0.25));
        int beaval = (int)(Math.round(nSize * 0.1));

        if (pitval < 1)
          pitval = 1;

        if (beaval < 1)
          beaval = 1;

        System.out.println("\nPit Val: " + pitval);
        System.out.println("\nBeacon Val: " + beaval);

        // beacon
        for (i=0; i<beaval; i++) {
          System.out.println("Input BEACON " + (i+1) +  " X coordinate: ");
          nBeacon[i][0] = scan.nextInt();
          System.out.println("Input BEACON " + (i+1) +  " Y coordinate: "); // need to put validation
          nBeacon[i][1] = scan.nextInt();
        }

        for (i=0; i<beaval; i++)
          System.out.println(nBeacon[i][0] + " " + nBeacon[i][1]);

        //pit
        for (i=0; i<pitval; i++) {
          System.out.println("Input PIT " + (i+1) +  " X coordinate: ");
          nPit[i][0] = scan.nextInt();
          System.out.println("Input PIT " + (i+1) +  " Y coordinate: "); // need to put validation
          nPit[i][1] = scan.nextInt();
        }

        for (i=0; i<pitval; i++)
          System.out.println(nPit[i][0] + " " + nPit[i][1]);

    }

}
