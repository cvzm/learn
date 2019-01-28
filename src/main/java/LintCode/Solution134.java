package LintCode;



import java.util.*;

/**
 * 134. LRU缓存策略
 * @description 为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。
 * 获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。
 * 写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置。
 * @href https://www.lintcode.com/problem/lru-cache/description
 * @date: 2019-1-28
 */
public class Solution134 {

    public static class LRUCache {

        /**
         * 容量
         */
        private int capacity;

        /**
         * 数据集
         */
        private Map<Integer, Integer> map;


        /**
         * @param capacity: An integer
         */
        public LRUCache(int capacity) {
            this.capacity = capacity;
            this.map = new LinkedHashMap<>(this.capacity);
        }

        /**
         * @param key: An integer
         * @return: An integer
         */
        public int get(int key) {
            if (!map.containsKey(key))
                return -1;
            int val = map.remove(key);
            map.put(key, val);
            return val;

        }

        /**
         * @param key: An integer
         * @param value: An integer
         * @return: nothing
         */
        public void set(int key, int value) {
            if (map.containsKey(key)) {
                map.remove(key);
                map.put(key, value);
                return;
            }
            if (map.size() == capacity) {
                map.remove(map.entrySet().iterator().next().getKey());
            }
            map.put(key, value);
        }

    }

    public static void main(String[] args) {
        LRUCache lruCache = new LRUCache(3);
        lruCache.set(1,1);
        lruCache.set(2,2);
        lruCache.set(3,3);
        lruCache.set(4,4);
        System.out.println(lruCache.get(4));
        System.out.println(lruCache.get(3));
        System.out.println(lruCache.get(2));
        System.out.println(lruCache.get(1));
        lruCache.set(5,5);
        System.out.println(lruCache.get(1));
        System.out.println(lruCache.get(2));
        System.out.println(lruCache.get(3));
        System.out.println(lruCache.get(4));
        System.out.println(lruCache.get(5));

    }



}


