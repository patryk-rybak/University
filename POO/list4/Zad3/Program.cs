public class Reusable
{
      public void DoWork(){
            Console.WriteLine("work");
      }
}
public class ObjectPool
{
      private static ObjectPool _instance;
      private int _poolSize;
      private List<Reusable> _pool = new List<Reusable>();
      private List<Reusable> _acquired = new List<Reusable>();

      public static ObjectPool Instance
      {
            get
            {
                  if (_instance == null)
                  {
                        _instance = new ObjectPool(10);
                  }
                  return _instance;
            }
      }

      public ObjectPool(int poolSize)
      {
            if (poolSize <= 0)
            {
                  throw new ArgumentException();
            }
            this._poolSize = poolSize;
      }

      public Reusable AcquireReusable()
      {
            if (_acquired.Count == this._poolSize)
            {
                  throw new ArgumentException("Pool is full.");
            }

            if (_pool.Count == 0)
            {
                  var reusable = new Reusable();
                  _pool.Add(reusable);
            }

            var element = _pool[0];
            _pool.Remove(element);
            _acquired.Add(element);
            return element;
      }

      public void ReleaseReusable(Reusable reusable)
      {
            if (!_acquired.Contains(reusable))
            {
                  throw new ArgumentException("The resource is not in the acquired list.");
            }

            _acquired.Remove(reusable);
            _pool.Add(reusable);
      }
}




public class BetterReusable
{
      private Reusable _reusable;
      private bool _isReleased;

      // usyzskuje doste do puli
      public BetterReusable()
      {
            _reusable = ObjectPool.Instance.AcquireReusable();
            _isReleased = false;
      }

      // zwraca do puli
      public void Release()
      {
            if (_isReleased)
            {
                  throw new InvalidOperationException("The resource has already been released.");
            }

            ObjectPool.Instance.ReleaseReusable(_reusable);
            _isReleased = true;
      }

      // deelguje do reasable
      public void DoWork()
      {
            if (_isReleased)
            {
                  throw new InvalidOperationException("Cannot perform work on a released resource.");
            }

            _reusable.DoWork();
      }
}



public class Program
{
      public static void Main()
      {
            var reusable = new BetterReusable();
            reusable.DoWork();
            reusable.Release();
      }
}
