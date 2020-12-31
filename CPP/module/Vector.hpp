//
// Created by HosodaMath on 2020/12/28.
//
#pragma once
#include <iostream>
#include <cmath>
namespace math
{
    class Vector2
    {
    private:
        double x;
        double y;

    public:
        Vector2() noexcept = default;

        ///2次元ベクトル
        ///example1
        ///double x1 = 5.0, y1 = 5.0;
        ///math::Vector2 locaiton1(x1, y1);
        ///double x2 = 2.0, y2 = 9.0;
        ///math::Vector2 locaiton2(x2, y2);
        ///
        ///example2
        ///double x3 = 5.0, y3 = 5.0;
        ///math::Vector2 locaiton3(x3, y3);
        ///double x4 = 2.0, y4 = 9.0;
        ///math::Vector2 locaiton4(x4, y4);
        constexpr Vector2(double _init_x, double _init_y) : x(_init_x), y(_init_y) {}

        ///get vector x value
        ///example
        ///location3.get_x(); -> 5.0
        ///location4.get_x(); -> 2.0
        [[nodiscard]] constexpr double get_x() const noexcept { return x; }

        ///get vector y value
        ///example1
        ///location3.get_y(); -> 5.0
        ///location4.get_y(); -> 9.0
        [[nodiscard]] constexpr double get_y() const noexcept { return y; };

        ///足し算
        [[nodiscard]] constexpr Vector2 operator+() const noexcept { return *this; }

        /// negative vector
        /// example1
        ///-locaiton1 -> (-5, -5)
        ///-location4 -> (-2, -9)
        [[nodiscard]] constexpr Vector2 operator-() const noexcept { return Vector2(-x, -y); }

        /// ベクトルの足し算
        /// example1
        /// locaiton1 + locaiton2 -> (7, 14)
        [[nodiscard]] constexpr Vector2 operator+(const Vector2 &other_value) const noexcept
        {
            return Vector2(x + other_value.x, y + other_value.y);
        }

        /// ベクトルの引き算
        /// example1
        /// locaiton1 - locaiton2 -> (3, -4)
        [[nodiscard]] constexpr Vector2 operator-(const Vector2 &other_value) const noexcept
        {
            return Vector2(x - other_value.x, y - other_value.y);
        }

        /// ベクトルの掛け算(かける値は原則スカラー値)
        /// example1
        /// locaiton1 * m -> (25, 25)
        /// locaiton2 * m -> (10, 45)
        [[nodiscard]] constexpr Vector2 operator*(const double &other_value) const noexcept
        {
            return Vector2(x * other_value, y * other_value);
        }

        /// ベクトルの割り算(割る値は原則スカラー値)
        /// example1
        /// locaiton1 / d -> (1.66667, 1.66667)
        /// locaiton2 / d -> (0.666667, 3)
        [[nodiscard]] constexpr Vector2 operator/(const double &other_value) const noexcept
        {
            return Vector2(x / other_value, y / other_value);
        }

        /// ベクトルの足し算
        /// example2
        /// locaiton3 += locaiton4;
        constexpr Vector2 &operator+=(const Vector2 &value) noexcept
        {
            x += value.x;
            y += value.y;

            return *this;
        }

        /// ベクトルの引き算
        /// example2
        /// locaiton3 -= locaiton4;
        constexpr Vector2 &operator-=(const Vector2 &value) noexcept
        {
            x -= value.x;
            y -= value.y;

            return *this;
        }

        /// ベクトルの掛け算
        /// example2
        /// locaiton3 *= m2;
        /// locaiton4 *= m2;
        constexpr Vector2 &operator*=(double &value) noexcept
        {
            x *= value;
            y *= value;

            return *this;
        }

        /// ベクトル同士の掛け算
        /// example2
        /// locaiton3 *= m2;
        /// locaiton4 *= m2;
        constexpr Vector2 &operator*=(const Vector2 &value) noexcept
        {
            x *= value.x;
            y *= value.y;

            return *this;
        }

        /// ベクトルの割り算
        /// example2
        /// locaiton3 /= d2;
        /// locaiton4 /= d2;
        constexpr Vector2 &operator/=(double &value) noexcept
        {
            x /= value;
            y /= value;

            return *this;
        }

        /// ベクトル同士の割り算
        /// example2
        /// locaiton3 *= m2;
        /// locaiton4 *= m2;
        constexpr Vector2 &operator/=(const Vector2 &value) noexcept
        {
            x /= value.x;
            y /= value.y;

            return *this;
        }

        ///calc  squared magnitude
        [[nodiscard]] constexpr double magSq() const noexcept
        {
            return magSqCalc(*this);
        }

        [[nodiscard]] static constexpr double magSqCalc(const Vector2 &vec_value) noexcept
        {
            return vec_value.x * vec_value.x + vec_value.y * vec_value.y;
        }

        ///calc  magnitude
        [[nodiscard]] double magnitude() const noexcept
        {
            return sqrt(magSq());
        }

        ///dot product
        [[nodiscard]] constexpr double dot(const Vector2 &vec_value) const noexcept
        {
            return x * vec_value.x + y * vec_value.y;
        }

        ///cross product
        [[nodiscard]] constexpr double cross(const Vector2 &vec_value) const noexcept
        {
            return x * vec_value.x - y * vec_value.y;
        }

        ///x and y equal
        [[nodiscard]] constexpr bool operator==(const Vector2 &value) const noexcept
        {
            return x == value.x && y == value.y;
        }

        ///x and y not equal
        [[nodiscard]] constexpr bool operator!=(const Vector2 &value) const noexcept
        {
            return x != value.x && y != value.y;
        }
    };

    inline std::ostream &operator<<(std::ostream &s, const Vector2 &value)
    {
        return s << "(" << value.get_x() << ", " << value.get_y() << ")";
    }

} // namespace math



