using System;
using System.Collections.Generic;

public class Context
{
    private Dictionary<string, bool> variables = new Dictionary<string, bool>();

    public bool GetValue(string variableName)
    {
        if (!variables.ContainsKey(variableName))
            throw new Exception($"zmienna '{variableName}' nie została zdefiniowana w kontekście.");

        return variables[variableName];
    }

    public bool SetValue(string variableName, bool value)
    {
        variables[variableName] = value;
        return true;
    }
}

public abstract class AbstractExpression
{
    public abstract bool Interpret(Context context);
}


public class ConstExpression : AbstractExpression
{
    private bool value;

    public ConstExpression(bool value)
    {
        this.value = value;
    }

    public override bool Interpret(Context context)
    {
        return value;
    }
}


public class VariableExpression : AbstractExpression
{
    private string name;

    public VariableExpression(string name)
    {
        this.name = name;
    }

    public override bool Interpret(Context context)
    {
        return context.GetValue(name);
    }
}


public class UnaryExpression : AbstractExpression
{
    private AbstractExpression expression;

    public UnaryExpression(AbstractExpression expression)
    {
        this.expression = expression;
    }

    public override bool Interpret(Context context)
    {
        return !expression.Interpret(context);
    }
}


public enum BinaryOperator
{
    And,
    Or
}

public class BinaryExpression : AbstractExpression
{
    private AbstractExpression left;
    private AbstractExpression right;
    private BinaryOperator op;

    public BinaryExpression(AbstractExpression left, AbstractExpression right, BinaryOperator op)
    {
        this.left = left;
        this.right = right;
        this.op = op;
    }

    public override bool Interpret(Context context)
    {
        bool leftVal = left.Interpret(context);
        bool rightVal = right.Interpret(context);

        return op switch
        {
            BinaryOperator.And => leftVal && rightVal,
            BinaryOperator.Or => leftVal || rightVal,
            _ => throw new Exception("nieznany operator binarny.")
        };
    }
}

public class Program
{
    public static void Main()
    {
        Context ctx = new Context();
        ctx.SetValue("x", false);
        ctx.SetValue("y", true);

        // !(x && y) || true
        AbstractExpression expression =
            new BinaryExpression(
                new UnaryExpression(
                    new BinaryExpression(
                        new VariableExpression("x"),
                        new VariableExpression("y"),
                        BinaryOperator.And
                    )
                ),
                new ConstExpression(true),
                BinaryOperator.Or
            );

        bool result = expression.Interpret(ctx);
        Console.WriteLine($"wynik wyrażenia: {result}");
        try
        {
            AbstractExpression invalidExpression = new VariableExpression("z");
            bool invalidResult = invalidExpression.Interpret(ctx);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"mamy wyjątek: {ex.Message}");
        }
    }
}
