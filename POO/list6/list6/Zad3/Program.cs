public abstract class Tree
{
    public abstract int Accept(Visitor visitor);
}

public class TreeLeaf : Tree
{
    public override int Accept(Visitor visitor)
    {
        return visitor.VisitLeaf(this);
    }
}

public class TreeNode : Tree
{
    public Tree Left { get; set; }
    public Tree Right { get; set; }

    public override int Accept(Visitor visitor)
    {
        return visitor.VisitNode(this);
    }
}


public abstract class Visitor
{
    public abstract int VisitNode(TreeNode node);
    public abstract int VisitLeaf(TreeLeaf leaf);
}

public class ConcreteDepthVisitor : Visitor
{
    public override int VisitLeaf(TreeLeaf leaf)
    {
        return 1;
    }

    public override int VisitNode(TreeNode node)
    {
        int leftDepth = node.Left != null ? node.Left.Accept(this) : 0;
        int rightDepth = node.Right != null ? node.Right.Accept(this) : 0;
        return 1 + Math.Max(leftDepth, rightDepth);
    }
}


public class Program
{
    public static void Main()
    {
        Tree root = new TreeNode
        {
            Left = new TreeNode
            {
                Left = new TreeNode{
                    Left = new TreeLeaf(),
                    Right = null
                },
                Right = new TreeLeaf()
            },
            Right = new TreeLeaf()
        };

        ConcreteDepthVisitor depthVisitor = new ConcreteDepthVisitor();
        int depth = root.Accept(depthVisitor);
        Console.WriteLine($"głębokość drzewa: {depth}");
    }
}
