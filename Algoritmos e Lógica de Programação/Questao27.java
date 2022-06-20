public class Tabela {
    public static void main(String args[]) {
      int tabela [] [] = new int [2] [2];
      
      tabela [0] [0] = 12;
      tabela [1] [0] = 21;
      tabela [0] [1] = 26;
      tabela [1] [1] = 45;
      
      System.out.print(tabela [0] [0] + " ");
      System.out.print(tabela [0] [1] + "\n");
      System.out.print(tabela [1] [0] + " ");
      System.out.print(tabela [1] [1] + " ");
    }
}