/*
 * Copyright (c) 2020, Open Source Robotics Foundation.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the copyright holder nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#pragma(once)

#include <SDL2/SDL.h>
#include <chrono>
#include <future>
#include <memory>
#include <string>
#include <thread>
#include <vector>

using namespace std::chrono;

namespace xyber_x1_infer::joy_stick_module {

struct JoyStruct {
  std::vector<double> axis;
  std::vector<int32_t> buttons;
};

class Joy {
 public:
  explicit Joy();
  Joy(Joy&& c) = delete;
  Joy& operator=(Joy&& c) = delete;
  Joy(const Joy& c) = delete;
  Joy& operator=(const Joy& c) = delete;

  ~Joy();

  void GetJoyData(JoyStruct& joy_data);

 private:
  void eventThread();
  bool handleJoyAxis(const SDL_Event& e);
  bool handleJoyButtonDown(const SDL_Event& e);
  bool handleJoyButtonUp(const SDL_Event& e);
  bool handleJoyHatMotion(const SDL_Event& e);
  void handleJoyDeviceAdded(const SDL_Event& e);
  void handleJoyDeviceRemoved(const SDL_Event& e);
  float convertRawAxisValueToROS(int16_t val);

  int dev_id_{0};

  SDL_Joystick* joystick_{nullptr};
  SDL_Haptic* haptic_{nullptr};
  int32_t joystick_instance_id_{0};
  double scaled_deadzone_{0.0};
  double unscaled_deadzone_{0.0};
  double scale_{0.0};
  double autorepeat_rate_{0.0};
  int autorepeat_interval_ms_{0};
  bool sticky_buttons_{false};
  bool publish_soon_{false};
  time_point<high_resolution_clock> publish_soon_time_;
  int coalesce_interval_ms_{0};
  std::string dev_name_;
  std::thread event_thread_;
  std::atomic_bool is_runnig_{true};

  std::mutex joy_msg_mutex_;
  std::atomic_bool is_update_{false};
  JoyStruct joy_msg_;
};

}  // namespace xyber_x1_infer::joy_stick_module
