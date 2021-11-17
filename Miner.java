import java.util.*;

public class Miner{

  private int posX;
  private int posY;
  private int frontX;
  private int frontY;

// getters
  public int getposX(){
    return this.posX;
  }

  public int getposY(){
    return this.posY;
  }

  public int getfrontX(){
    return this.frontX;
  }

  public int getfrontY(){
    return this.frontY;
  }

// setter
  public void setposX(int X){
    this.posX = X;
  }

  public void setposY(int Y){
    this.posY = Y;
  }

  public void setfrontX(int X){
    this.frontX = X;
  }

  public void setfrontY(int Y){
    this.frontY = Y;
  }

  public void move(){
    this.posX = this.frontX;
    this.posY = this.frontY;
  }
}
