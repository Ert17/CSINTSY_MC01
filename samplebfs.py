import java.util.LinkedList;
import java.util.Queue;

//
// Decompiled by Procyon v0.5.36
//

public class BFS
{
    public static int[][] maze;

    public BFS(final int[][] g) {
        BFS.maze = g;
    }

    public static class Point {
        int x;
        int y;
        Point parent;

        public Point(int x, int y, Point parent) {
            this.x = x;
            this.y = y;
            this.parent = parent;
        }

        public Point getParent() {
            return this.parent;
        }

        public String toString() {
            return "x = " + x + " y = " + y;
        }
  }

    public static Queue<Point> q = new LinkedList<Point>();
    public static Point getPathBFS(int x, int y) {
        q.add(new BFS.Point(x, y, (BFS.Point)null));
        while (!BFS.q.isEmpty()) {
            final BFS.Point p = BFS.q.remove();
            System.out.println(BFS.maze[0][0]);
            if (BFS.maze[p.x][p.y] == 9) {
                System.out.println("Exit is reached!");
                return p;
            }
            if (isFree(p.x + 1, p.y)) {
                BFS.maze[p.x][p.y] = -1;
                final BFS.Point nextP = new BFS.Point(p.x + 1, p.y, p);
                BFS.q.add(nextP);
            }
            if (isFree(p.x - 1, p.y)) {
                BFS.maze[p.x][p.y] = -1;
                final BFS.Point nextP = new BFS.Point(p.x - 1, p.y, p);
                BFS.q.add(nextP);
            }
            if (isFree(p.x, p.y + 1)) {
                BFS.maze[p.x][p.y] = -1;
                final BFS.Point nextP = new BFS.Point(p.x, p.y + 1, p);
                BFS.q.add(nextP);
            }
            if (!isFree(p.x, p.y - 1)) {
                continue;
            }
            BFS.maze[p.x][p.y] = -1;
            final BFS.Point nextP = new BFS.Point(p.x, p.y - 1, p);
            BFS.q.add(nextP);
        }
        return null;
    }

    public static boolean isFree(final int x, final int y) {
        return x >= 0 && x < BFS.maze.length && y >= 0 && y < BFS.maze[x].length && (BFS.maze[x][y] == 0 || BFS.maze[x][y] == 9 || BFS.maze[x][y] == 2);
    }
}
